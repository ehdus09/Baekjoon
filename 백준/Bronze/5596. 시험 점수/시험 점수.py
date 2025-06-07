mi, mm, ms, me = map(int, input().split())
si, sm, ss, se = map(int, input().split())
s = mi + mm + ms + me
t = si + sm + ss + se
if s >= t:
    print(s)
else:
    print(t)