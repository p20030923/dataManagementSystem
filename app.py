mode_msg = """
--- 人事資料管理系統 ---
1. 新增資料
2. 查詢資料
3. 修改資料
4. 刪除資料
5. 顯示所有資料
6. 退出系統
------------------------
"""
data_set = []

def mode1_add():
    loop = True
    while loop:
        dept = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        while True:
            try:
            # 執行可能引發異常的程式區塊
                age = input("請輸入年齡: ")
            except Exception as e:
                # 處理相應例外的程式碼
                print(f"錯誤訊息為{e}")
                print("請輸入阿拉伯數字")
            else:
                # 當try程式區塊成功執行時，會執行此區塊的程式碼(可省略)
                break
        phone = input("請輸入手機號碼: ")
        data = {"dept":dept, "name":name, "age":age, "phone":phone}
        data_set.append(data)
        while True:
            next = input("是否繼續新增資料? (y/n): ")
            if next == 'y' or next == "Y":
                break
            if next == 'n' or next == "N":
                loop = False
                break
            print("輸入有誤 請重新輸入")

def mode2_check():
    in_data_set = False
    name = input("請輸入要查詢的姓名: ")
    print("--- 查詢結果 ---")
    print("部門\t姓名\t年齡\t手機")
    print("----------------------------------------")
    for data in data_set:
        if data["name"] == name:
            in_data_set = True
            for i in data:
                print(data[i], "\t", end="")
            print()
    if in_data_set == False:
        print("查無此人")

def mode3_edit():
    in_data_set = False
    name = input("請輸入要修改的姓名: ")
    print("--- 當前資料 ---")
    print("部門\t姓名\t年齡\t手機")
    print("----------------------------------------")
    for data in data_set:
        if data["name"] == name:
            in_data_set = True
            for i in data:
                print(data[i], "\t", end="")
            print()
    if in_data_set == False:
        print("查無此人")
    else:
        while True:
            print("\n1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機")
            try:
            # 執行可能引發異常的程式區塊
                column = int(input("請輸入要修改的欄位: "))
            except Exception as e:
                # 處理相應例外的程式碼
                print(f"錯誤訊息為{e}")
                print("請輸入阿拉伯數字 1 ~ 4")
            else:
                # 當try程式區塊成功執行時，會執行此區塊的程式碼(可省略)
                if column == 1:
                    new = input("請輸入新的部門: ")
                    for data in data_set:
                        if data["name"] == name:
                            data["dept"] = new
                            break
                    break
                elif column == 2:
                    new = input("請輸入新的姓名: ")
                    for data in data_set:
                        if data["name"] == name:
                            data["name"] = new
                            break
                    break
                elif column == 3:
                    while True:
                        try:
                        # 執行可能引發異常的程式區塊
                            new = input("請輸入新的年齡: ")
                        except Exception as e:
                            # 處理相應例外的程式碼
                            print(f"錯誤訊息為{e}")
                            print("請輸入阿拉伯數字")
                        else:
                            # 當try程式區塊成功執行時，會執行此區塊的程式碼(可省略)
                            break
                    for data in data_set:
                        if data["name"] == name:
                            data["age"] = new
                            break
                    break
                elif column == 4:
                    new = input("請輸入新的手機號碼: ")
                    for data in data_set:
                        if data["name"] == name:
                            data["phone"] = new
                            break
                    break
                else:
                    print("請輸入阿拉伯數字 1 ~ 4")
                    continue
        print("--- 更新後的資料 ---")
        print("部門\t姓名\t年齡\t手機")
        print("----------------------------------------")
        for data in data_set:
            if data["name"] == name:
                for i in data:
                    print(data[i], "\t", end="")
                print()

def mode4_del():
    in_data_set = False
    name = input("請輸入要刪除的姓名: ")
    for data in data_set:
        if data["name"] == name:
            in_data_set = True
    if in_data_set == False:
        print("查無此人")
    else:
        while True:
            next = input(f"確定要刪除 {name} 的資料嗎? (y/n): ")
            if next == 'y' or next == "Y":
                for data in data_set:
                    if data["name"] == name:
                        data_set.remove(data)
                        print(f"{name} 的資料已刪除")
                        print("--- 剩餘的所有資料 ---")
                        print("部門\t姓名\t年齡\t手機")
                        print("----------------------------------------")
                        for data in data_set:
                            for i in data:
                                print(data[i], "\t", end="")
                            print()
                break
            if next == 'n' or next == "N":
                break
            print("輸入有誤 請重新輸入")


def mode5_display():
    print("部門\t姓名\t年齡\t手機")
    print("----------------------------------------")
    for data in data_set:
        for i in data:
            print(data[i], "\t", end="")
        print()



while True:
    print(mode_msg)
    try:
    # 執行可能引發異常的程式區塊
        mode = int(input("請選擇功能: "))
    except Exception as e:
        # 處理相應例外的程式碼
        print(f"錯誤訊息為{e}")
        print("請輸入阿拉伯數字 1 ~ 6")
    else:
        # 當try程式區塊成功執行時，會執行此區塊的程式碼(可省略)
        if mode == 1:
            mode1_add()
        elif mode == 2:
            mode2_check()
        elif mode == 3:
            mode3_edit()
        elif mode == 4:
            mode4_del()
        elif mode == 5:
            mode5_display()
        elif mode == 6:
            print("系統已退出")
            break
        else:
            print("請輸入阿拉伯數字 1 ~ 6")
            continue
    finally:
        # 無論try程式區塊是否發生異常，都執行finally程式碼區塊的程式碼(可省略)
        pass

