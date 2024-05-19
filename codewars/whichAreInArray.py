def in_array(array1, array2):
    output = []
    for r1 in array1:
        for r2 in array2:
            if r1 in r2:
                if r1 in output:
                    continue
                output.append(r1)
    return sorted(output)


print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
