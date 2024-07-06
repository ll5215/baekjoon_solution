t = int(input())

li = []
for _ in range(t):
    n = int(input())
    if n in li:
        False
    else:
        li.append(n)

        for i in range(len(li)):
            m_index=i
            for j in range(i +1,len(li)):
                if li[j] < li[m_index]:
                    m_index=j
            li[i], li[m_index] = li[m_index], li[i] 

for s in li:
    print(s)