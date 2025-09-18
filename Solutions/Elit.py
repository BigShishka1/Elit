# 1 задание--------------------------------------------------------------------
# def is_true(s):
#     stack = []
#
#     pairs = {')': '(', ']': '[', '}': '{'}
#
#     for char in s:
#         if char in pairs:
#             if not stack or stack.pop() != pairs[char]:
#                 return False
#         else:
#             stack.append(char)
#
#     return not stack
#
# s = input("Введите строку со скобками: ")
#
# print(is_true(s))

# 2 задание------------------------------------------------------------------

# def massive(nums1, m, nums2, n):
#
#     i = m - 1
#     j = n - 1
#     k = m + n - 1
#
#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
#
#     while j >= 0:
#         nums1[k] = nums2[j]
#         j -= 1
#         k -= 1
#
# print("Введите элементы первого массива nums1 через пробел:")
# nums1 = list(map(int, input().split()))
#
# print("Введите количество элементов m в первом массиве:")
# m = int(input())
#
# print("Введите элементы второго массива nums2 через пробел:")
# nums2 = list(map(int, input().split()))
#
# print("Введите количество элементов n во втором массиве:")
# n = int(input())
#
# nums1 = nums1[:m] + [0] * n
#
# massive(nums1, m, nums2, n)
# print("Объединенный отсортированный массив:")
# print(nums1)

#3 задание------------------------------------------------------------------------

# prices = list(map(int, input("Введите цены через пробел: ").split()))
# min_price = float('inf')
# max_value = 0
#
# for price in prices:
#     if price < min_price:
#         min_price = price
#     elif price - min_price > max_value:
#         max_value = price - min_price
#
# print(f"Максимальная прибыль: {max_value}")

#4 задание--------------------------------------------------------------------------

s = input("Введите первое слово: ")
t = input("Введите второе слово: ")
if sorted(s) != sorted(t):
    print(False)
else:
    print(True)

#5 задание---------------------------------------------------------

# from collections import deque
#
# class RecentCounter:
#     def init(self):
#         self.queue = deque()
#
#     def ping(self, t: int) -> int:
#         self.queue.append(t)
#         while self.queue[0] < t - 3000:
#             self.queue.popleft()
#         return len(self.queue)
#
# # Пример использования
# if __name__ == "__main__":
#     recentCounter = RecentCounter()
#     print(recentCounter.ping(1))
#     print(recentCounter.ping(100))
#     print(recentCounter.ping(3001))
#     print(recentCounter.ping(3002))


