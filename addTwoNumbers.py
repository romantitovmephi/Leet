# несвязные списки
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]


class Solution:
    def addTwoNumbers(self, l1, l2):
        # получаем "обратное" число из списка l1
        str_item_l1 = [str(i) for i in l1]
        str_number_l1 = ''.join(str_item_l1)
        reverse_number_l1 = str_number_l1[::-1]
        int_reverse_number_l1 = int(reverse_number_l1)

        # получаем "обратное" число из списка l2
        str_item_l2 = [str(i) for i in l2]
        str_number_l2 = ''.join(str_item_l2)
        reverse_number_l2 = str_number_l2[::-1]
        int_reverse_number_l2 = int(reverse_number_l2)

        result_num = int_reverse_number_l1 + int_reverse_number_l2

        # строку можно инвер-ть
        str_result_num = str(result_num)
        reverse_str_result_num = str_result_num[::-1]

        list_reverse_str_result_num = list(reverse_str_result_num)

        int_list_reverse_str_result_num = [
            int(i) for i in list_reverse_str_result_num]

        return int_list_reverse_str_result_num


evaluate = Solution()
print(evaluate.addTwoNumbers(l1, l2))
