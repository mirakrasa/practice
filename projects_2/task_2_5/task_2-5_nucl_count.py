print('=== Анализ последовательности ДНК ===')

s = input('Введите последовательность ДНК: ').upper()

A = s.count('A')
T = s.count('T')
G = s.count('G')
C = s.count('C')

print(f'Последовательность в верхнем регистре: {s}')
print('Подсчёт нуклеотидов:')
print()
print(f'A: {A}')
print(f'T: {T}')
print(f'G: {G}')
print(f'C: {C}')
print()
print(f'Общая длина: {len(s)} нуклеотидов')