if __name__ == '__main__':
    records=[];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_highest = sorted(set([score for name, score in records]))[1]
    print('\n'.join(sorted([name for name, score in records if score == second_highest])))
        