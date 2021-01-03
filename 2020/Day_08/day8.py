# Part 1
print(
	(	# Deklarujemy funkcję execute, która przyjmuje 4 argumenty:
		# data.txt - listę linii z pliczku
		# line - nr linii, którą rozpatrujemy
		# acc - wartość akumulatora po wywołaniu instrukcji pod linią line
		# listę odwiedzonych indeksów (linii)
		# Funkcja zadeklarowana walrusem i lambdą co znaczy, że się deklaruje
		# i od razu wywołuje dla zadanych argumentów w miejscu x
		execute := lambda input, line, acc, visited:
			# Funkcja zwraca aktualny akumulator kiedy odwiedzana linia była już odwiedzana
			acc if line in visited
			# W przeciwnym wypadku...
			else (
				# ...wywołujemy naszą funkcję rekurencyjnie dalej...
				execute(
					# ...podając jako pierwszy argument wciąż nasz data.txt...
					input,
					# ...jako drugi następną linię kiedy mamy instrukcję 'nop' lub 'acc'
					# albo linię oddaloną o argument w jmp (else to jmp, bo innej instrukcji nie mamy)...
					line + 1 if input[line].startswith(('nop', 'acc')) else line + int(input[line][4:]),
					# ...jako kolejny argument to akumulator powiększony o wartość przy instrukcji acc
					# albo niezmieniony akumulator w przypadku else (innej instrukcji)...
					acc + int(input[line][4:]) if input[line].startswith('acc') else acc,
					# ...i jako ostatni argument to lsita odwiedzonych powiększona o aktualną linię
					visited + [line]
				)
			)
	)
	(open('data.txt').readlines(), 0, 0, [])  # To są zadane startowo argumenty (miejsce x)
	# Na starcie mamy nasz plik wejściowy,
	# 0 jako pierwszą linię,
	# 0 jako startowy akumulator,
	# pustą tablicę odwiedzonych (bo żadnej linii jeszcze nie wykonaliśmy)
)

# Part 2
print(	# Sumuje wyniki każdej z kopii (tylko jeden wynik jest różny od zera, toteż ten wynik nam zwróci funkcja sum()
        sum(map(  # Funkcja map, która wykonuje funkcję z poprzedniej części na każdej kopii inputu ze zmienioną odpowiednią linią
            execute := lambda input, line=0, acc=0, visited=[]:  # Jako data.txt jest przekazany wynik funkcji poniżej (lista kopii)
				# Reszta argumentów jest ustawiona domyślnie jako słowa kluczowe, więc nie trzeba (i nie można) nic więcej przekazać
                acc if line >= len(input)  # Modyfikacja - teraz funkcja zwraca wartość akumulatora kiedy udało się wyjść z programu
				else (
                    0 if line in visited  # W innym wypadku zwraca 0
					else (
						execute(
							input,
							line + 1 if input[line].startswith(('nop', 'acc')) else line + int(input[line][4:]),
							acc + int(input[line][4:]) if input[line].startswith('acc') else acc,
							visited + [line]
						)
                    )
                ),
            (lambda input:  # Deklaracja funkcji, która każdej linii w inpucie przyporządkowuje kopię inputu ze zmienioną linią (lambdą, więc od razu funkcja się wykona)
                [[c_line.replace('jmp', 'n').replace('nop', 'jmp').replace('n', 'nop') if c_idx == o_idx else c_line for c_idx, c_line in enumerate(input.copy())]
				 for o_idx, o_line in enumerate(input)]
             )(open('data.txt').readlines())  # Przekazujemy do powyższej funkcji w argumencie nasz data.txt
        )
    )
)
