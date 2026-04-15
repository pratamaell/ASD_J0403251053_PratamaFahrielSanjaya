def merge_sort (data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    data_kiri = data[:mid]
    data_kanan = data [mid:]

    kiri_sorted = merge_sort(data_kiri)
    kanan_sorted = merge_sort(data_kanan)

    return merge(kiri_sorted, kanan_sorted)

def merge (data_kiri, data_kanan):
    result = []
    i = j = 0

    while i < len(data_kiri) and j < len(data_kanan):
        if data_kiri[i] <= data_kanan[j]:
            result.append(data_kiri[i])
            i +=1
        else:
            result.append(data_kanan[j])
            j += 1

    result.extend(data_kiri[i:])
    result.extend(data_kanan[j:])

    return result