# Exercicio 01
def max_consecutive_sum(lista):
    max_sum = lista[0]
    current_sum = lista[0]

    for i in range(1, len(lista)):
        current_sum += lista[i]


        if lista[i] > current_sum:
          current_sum = lista[i]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Testes 01
def test_max_consecutive_sum():
    print(max_consecutive_sum([1, -3, 2, 1, -1]) == 3)
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7)
    print(max_consecutive_sum([1]) == 1)
    print(max_consecutive_sum([-1, -2, -3, -4, -5]) == -1)


# Exercício 02
def is_palindrome(string):
    #tirando maiúscula
    string = string.replace(" ", "").lower()

    if string == string[::-1]:  
        return True
    else:
        return False

# Testes 02
def text_is_palindrome():
    print(is_palindrome("radar") == True)
    print(is_palindrome("racecar") == True)
    print(is_palindrome("level") == True)
    # Testes negativos
    print(is_palindrome("python") == False)
    print(is_palindrome("hello") == False)
    print(is_palindrome("12321") == False)
    print(is_palindrome("abccbaa") == False)


# Exercício 03
def contar_subconjuntos_crescentes(numeros):
    total = 0
    
    for i in range(len(numeros)):
        subconjunto = [numeros[i]]
        
        for j in range(i + 1, len(numeros)):
            if numeros[j] > subconjunto[-1]:
                subconjunto.append(numeros[j])
                total += 1
        
        total += 1  
        
    return total

# Testes 03
def test_count_increasing_subsets():
    # Teste com lista vazia
    print(count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]) == 8)
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 16)


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
