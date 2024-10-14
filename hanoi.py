def solve(n, source, target, auxillary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    solve(n-1, source, auxillary, target)
    print(f"Move disk {n} from {source} to {target}")

    solve(n-1, auxillary, target, source)


n = 3
solve(n, 'A', 'C', 'B')
