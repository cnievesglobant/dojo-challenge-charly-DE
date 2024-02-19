def jump_game(nums):
    n= len(nums)
    saltos = 0
    actual = 0
    fin= 0

    for i in range(n-1):
        fin= max(fin, i + nums[i])

        if i == actual:
            saltos += 1
            actual = fin
            
    return saltos


nums  =  [2,3,1,1,4]
#nums = [2,3,0,1,4]
print(jump_game(nums))

print("¡Adiós!")

