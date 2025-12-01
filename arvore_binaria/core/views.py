# core/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BSTSession, BinarySearchTree
import json

# ==========================================
# RENDERIZAÇÃO DA PÁGINA
# ==========================================

def index(request):
    """Renderiza a página inicial (home.html)."""
    return render(request, 'home.html')

# ==========================================
# FUNÇÕES DE MANIPULAÇÃO DA ÁRVORE (HELPER)
# ==========================================

def get_session_tree(request):
    """Helper para recuperar a árvore da sessão ou criar uma nova."""
    # Garante que a sessão existe
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    
    # Busca ou cria o objeto no banco de dados
    session_data, created = BSTSession.objects.get_or_create(
        session_key=session_key,
        defaults={'tree_data': 'null'}
    )
    
    return session_data, session_data.get_tree()

# ==========================================
# VIEWS DE API (AJAX) - Todas precisam de @csrf_exempt
# ==========================================

@csrf_exempt
def initialize_tree(request):
# ... (código omitido)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Recebe a lista de valores (já como números)
            valores = data.get('valores', []) 
            
            session_data, bst = get_session_tree(request)

            bst = BinarySearchTree()
            valores_inseridos = 0
            
            for valor in valores:
                try:
                    # Agora usamos 'valor' diretamente, pois o frontend já o converteu para JS Number
                    # A chamada int() aqui é apenas para sanear se for float ou string numérica
                    bst.insert(int(valor)) # <--- LINHA AJUSTADA (apenas para garantir o tipo)
                    valores_inseridos += 1
                except (ValueError, TypeError):
                    continue

            # FORÇA O BALANCEAMENTO APÓS A INSERÇÃO, usando o método corrigido
            if valores_inseridos > 0:
                bst.balance() 
            
            session_data.set_tree(bst)
            
            return JsonResponse({
                'success': True,
                'message': f'{valores_inseridos} valores inseridos e árvore balanceada.',
                'tree': bst.to_dict(),
                'in_order': bst.in_order()
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'JSON inválido.'}, status=400)
        except Exception as e:
            # Captura qualquer outro erro, como o antigo problema do balanceamento
            print(f"Erro ao inicializar: {e}")
            return JsonResponse({'success': False, 'message': f'Erro interno do servidor ao inicializar: {e}'}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def insert_value(request):
    """Insere um único valor na árvore."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            valor = int(data.get('valor')) # Conversão para int é garantida
            
            session_data, bst = get_session_tree(request)
            
            if bst.search(valor):
                return JsonResponse({
                    'success': False, 
                    'message': f'O valor {valor} já existe na árvore.'
                })
            
            bst.insert(valor)
            session_data.set_tree(bst)
            
            return JsonResponse({
                'success': True,
                'message': f'Valor {valor} inserido!',
                'tree': bst.to_dict(),
                'in_order': bst.in_order()
            })
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'message': 'Valor numérico inválido ou não fornecido.'}, status=400)
        except Exception as e:
            print(f"Erro ao inserir: {e}")
            return JsonResponse({'success': False, 'message': f'Erro interno do servidor ao inserir: {e}'}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def delete_value(request):
    """Remove um único valor da árvore."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            valor = int(data.get('valor'))
            
            session_data, bst = get_session_tree(request)
            
            deleted = bst.delete(valor)
            
            if deleted:
                session_data.set_tree(bst) # Salva o estado após a deleção
                return JsonResponse({
                    'success': True,
                    'message': f'Valor {valor} removido com sucesso.',
                    'tree': bst.to_dict(),
                    'in_order': bst.in_order()
                })
            else:
                return JsonResponse({
                    'success': False, 
                    'message': f'Valor {valor} não encontrado na árvore.'
                })
                
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'message': 'Valor numérico inválido ou não fornecido.'}, status=400)
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return JsonResponse({'success': False, 'message': f'Erro interno do servidor ao deletar: {e}'}, status=500)

    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def search_value(request):
    """Busca um valor na árvore."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            valor = int(data.get('valor'))
            
            _, bst = get_session_tree(request)
            
            found = bst.search(valor)
            
            if found:
                message = f'Valor {valor} encontrado na árvore!'
            else:
                message = f'Valor {valor} não encontrado.'
                
            return JsonResponse({
                'success': True,
                'found': found,
                'message': message
            })
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'message': 'Valor numérico inválido ou não fornecido.'}, status=400)
        except Exception as e:
            print(f"Erro ao buscar: {e}")
            return JsonResponse({'success': False, 'message': f'Erro interno do servidor ao buscar: {e}'}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def balance_tree(request):
    """Rebalanceia a árvore manualmente usando DSW."""
    if request.method == 'POST':
        try:
            session_data, bst = get_session_tree(request)
            
            if bst.raiz is None:
                return JsonResponse({
                    'success': False,
                    'message': 'Árvore vazia, nada para rebalancear.'
                })

            bst.balance() # A chamada crítica ao método corrigido
            session_data.set_tree(bst)
            
            return JsonResponse({
                'success': True,
                'message': 'Árvore rebalanceada com sucesso usando DSW!',
                'tree': bst.to_dict(),
                'in_order': bst.in_order()
            })
            
        except Exception as e:
            # Se o erro 500 persistir, ele será capturado aqui
            print(f"Erro ao rebalancear: {e}")
            return JsonResponse({'success': False, 'message': f'Erro interno do servidor ao rebalancear: {e}'}, status=500)

    return JsonResponse({'success': False, 'message': 'Método não permitido.'}, status=405)


def get_tree(request):
    """Retorna o estado atual da árvore (usado ao recarregar a página)."""
    try:
        session_data, bst = get_session_tree(request)
        return JsonResponse({
            'tree': bst.to_dict(),
            'in_order': bst.in_order()
        })
    except Exception:
        # Retorna estrutura vazia em caso de falha de carregamento
        return JsonResponse({'tree': None, 'in_order': []})