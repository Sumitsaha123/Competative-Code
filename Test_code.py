def digit_manipulate(pos,len_num,manipulation_list,num):
    all_comb_list = []
    list_num = [x for x in str(num)]
    while(pos < len_num):
        for i in range(0, len(manipulation_list)):
            list_num[pos] = manipulation_list[i]
            str_num = ("".join(list_num))
            int_num = int(str_num)
            #print(int_num)
            if (int_num < 1000 or int_num > 9999 or int_num == num):
                continue
            else:
                diff = int_num - 1000
                all_comb_list.append(diff)

        pos += 1
        list_num = [x for x in str(num)]
    min_res = min(all_comb_list)
    if(len(out_list)== 0):
        out_list.append(min_res + 1000)
    else:
        while(out_list[len(out_list)-1] >= min_res+1000):
            all_comb_list.remove(min_res)
            min_res = min(all_comb_list)
        out_list.append(min_res + 1000)

input_list =[]
out_list = []
manipulation_list = ['0','1','2','3','4','5','6','7','8','9']
n = int(input("Please enter the length of the array:"))
pos = 0
for i in range(0,n):
    a=int(input())
    input_list.append(a)
for i in range(0,n):
    num = input_list[i]
    str_num = str(num)
    len_num = len(str_num)
    digit_manipulate(pos,len_num,manipulation_list,num)

print(out_list)

