def valley(steps,path ):
    altitud = 0
    valleys = 0
    in_valley = False

    for steps in path:
        if steps == 'U':  
            altitud += 1
        else:  
            altitud -= 1
        
        if altitud < 0 and not in_valley:
            in_valley = True
            valleys += 1
        
        if altitud == 0:
            in_valley = False
    
    return valleys

# Ejemplo de uso
steps = 8
path = "DDUUUUDDDDUUUUDDDDUUUUDD"
total_valleys = valley(steps, path)
print(f"On the walk they crossed  {total_valleys} valleys.")
