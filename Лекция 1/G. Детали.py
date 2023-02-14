N, K, M = map(int, input().split())
ans = 0
ost = N
qdet = K // M
ost2 = K - M * qdet
while ost >= K:
    qzag = ost // K
    ost1 = ost - K * qzag
    ost = ost1 + ost2 * qzag
    ans += qdet * qzag
print(ans)