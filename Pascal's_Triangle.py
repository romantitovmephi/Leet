numRows = 5


class Solution:
    def generate(self, numRows):
        empty_list = []
        list1 = [1]

        # создаем numRows кол-во списков с 1
        for n in range(1, numRows+1):
            empty_list.append(n*list1)

        # меняем 1 на значения по принципу треугольника Паскаля
        for i in range(2, numRows):
            for j in range(1, i):
                empty_list[i][j] = empty_list[i-1][j-1] + empty_list[i-1][j]
        pascal_list = empty_list
        # вернуть список рядов
        return pascal_list


pascal_rows = Solution()
print(pascal_rows.generate(numRows))
