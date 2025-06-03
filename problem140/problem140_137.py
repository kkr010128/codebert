base_txt = input()
base_txt_to_P = base_txt.replace("?","P")
base_txt_to_D = base_txt.replace("?","D")
index_count_base_txt_to_P = base_txt_to_P.count("D") + base_txt_to_P.count("PD")
index_count_base_txt_to_D = base_txt_to_D.count("D") + base_txt_to_D.count("PD")
if index_count_base_txt_to_P >index_count_base_txt_to_D:
    print(base_txt_to_P)
else:
    print(base_txt_to_D)