import itertools

def solve_cryptarithmetic():
    letters = "SENDMORY"  
    digits = "0123456789"
    
    for perm in itertools.permutations(digits, len(letters)):
        table = dict(zip(letters, perm))
        
       
        if table["S"] == "0" or table["M"] == "0":
            continue
        
        send = int("".join(table[c] for c in "SEND"))
        more = int("".join(table[c] for c in "MORE"))
        money = int("".join(table[c] for c in "MONEY"))
        
        if send + more == money:
            print("Solution Found!")
            print(f"SEND  = {send}")
            print(f"MORE  = {more}")
            print(f"MONEY = {money}")
            return  


if __name__ == "__main__":
    solve_cryptarithmetic()
