# """
# [401,403,404,405,407,408,409]
# [[401],[403,405],[407,409]]
#
# """
# seq = [401, 403, 404, 405, 407, 408, 409]
# start_index = 0
# result = []
# while start_index < len(seq):
#     end_result = None
#     jump = 1
#     start_num = seq[start_index]
#     end_index = start_index
#     while end_index < len(seq) -1:
#         end_index = start_index + jump
#         end_num = seq[end_index]
#         if end_num - start_num == jump:
#             end_result = end_num
#         else:
#             break
#         jump += 1
#     if end_result:
#         result.append([start_num, end_result])
#         start_index += jump
#     else:
#         result.append([start_num])
#         start_index += 1
# print(result)

# arr1 = [404, 401, 403, 409, 408, 405, 407]
#
# for i in range(len(arr1)):
#     for j in range(len(arr1)-1):
#         if arr1[j] > arr1[j+1]:
#             arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
# print(arr1)
#
# seq1 = [404, 401, 403, 409, 408, 405, 407]
# def mida(seq, l ,r):
#     i = l - 1
#     for j in range(l, r):
#         if seq[j] < seq[r]:
#             i += 1
#             seq[i], seq[j] = seq[j], seq[i]
#     seq[i+1], seq[r] = seq[r], seq[i+1]
#     return i
# def qui(seq, l, r):
#     if l < r:
#         mid = mida(seq, l, r)
#         qui(seq, l, mid)
#         qui(seq, mid+1, r)
# qui(seq1, 0, len(seq1)-1)
# print(seq)


seq = [6    , 1  ,  2   , 5]


def win():
    first = 0
    second = 0
    while len(seq) > 1:
        if seq[0] > seq[-1]:
            first += seq[0]
            seq.pop(0)
        else:
            first += seq[-1]
            seq.pop()

        if seq[0] > seq[-1]:
            second += seq[0]
            seq.pop(0)
        else:
            second += seq[-1]
            seq.pop()

    if len(seq) == 1:
        first += seq[0]

    return first > second


print(win())


