def stable(s1, s2, para):
    p_r = {}
    p_l = {}

    for l, r in para.items():
        p_r[r] = l
        p_l[l] = r

    is1 = {}
    is2 = {}

    for u in s1:
        is1[u] = {v: i for i, v in enumerate(s1[u])}
        
    for v in s2:
        is2[v] = {u: i for i, u in enumerate(s2[v])}


    for u in s1:
        for v in s2:
             if p_l[u] != v:
                # проверяем: хотят ли они друг друга больше текущих
                if (is1[u][v] < is1[u][p_l[u]] and
                    is2[v][u] < is2[v][p_r[v]]):
                    return False  # найдена блокирующая пара
    return True



s1 = {
    "Atlanta": ["Xavier", "Yolanda", "Zeus"],
    "Boston": ["Yolanda", "Xavier", "Zeus"],
    "Chicago": ["Xavier", "Yolanda", "Zeus"]
}

s2 = {
    "Xavier": ["Boston", "Atlanta", "Chicago"],
    "Yolanda": ["Atlanta", "Boston", "Chicago"],
    "Zeus": ["Atlanta", "Boston", "Chicago"]
}

para = {
    "Atlanta": "Xavier",
    "Boston": "Zeus",
    "Chicago": "Yolanda"
}



if stable(s1, s2, para):
    print("Устойчивое")
else:
    print("Неустойчивое")