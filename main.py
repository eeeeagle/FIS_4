import crypt
from tqdm import tqdm

val = "abcdefghijklmnopqrstuvwxyz"
code = "$6$ykRchyL.TIP/8JR4$.VY0IS6k.7pvLWUv3OUkqbJ4.PF.j2WzhaD.7.9SWyrHDPMg3m7h6Aj6zYoSFLN1HLKTueOeICSNBmDk67ApF/"
found_password = "----"

with tqdm(total=100) as progressbar:
    for first_symbol in val:
        for second_symbol in val:
            for third_symbol in val:
                for fourth_symbol in val:
                    password = first_symbol + second_symbol + third_symbol + fourth_symbol
                    if crypt.crypt(password, "$6$ykRchyL.TIP/8JR4$") == code:
                        found_password = password
                        break
                    progressbar.update(100/(26 ** 4))

print("\n\nPassword: ")
print(found_password)