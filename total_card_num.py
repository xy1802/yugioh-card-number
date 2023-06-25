import re

if __name__ == "__main__":
    text_list = []
    num_list = []
    acc = 0
    bag_acc=0

    num_list2 = []
    acc2 = 0
    bag_acc2=0
    with open("yugioh/view-source_https___ygocdb.com_packs.html",'r',encoding='utf-8') as fp:
        content = fp.read()
        # print(content)
        total = content.split('id</span>="<span class="html-attribute-value">tcg')
        print(total)
        matches = re.findall(r'class="html-tag">&lt;span&gt;</span>\d+<span class="html-tag">', total[0])
        # print(matches)
        # print(len(matches))
        for i in range(len(matches)):
            numbers = re.findall(r'\d+',matches[i])
            # print(numbers)
            num_list.append(numbers)
        print(num_list)
        for i in range(len(num_list)):
            if(int(num_list[i][0])<500):
                acc = acc+int(num_list[i][0])
                print(num_list[i][0])
                bag_acc+=1

        matches2 = re.findall(r'class="html-tag">&lt;span&gt;</span>\d+<span class="html-tag">', total[1])
        # print(matches)
        # print(len(matches))
        for i in range(len(matches2)):
            numbers2 = re.findall(r'\d+',matches2[i])
            # print(numbers)
            num_list2.append(numbers2)
        print(num_list2)
        for i in range(len(num_list2)):
            if(int(num_list2[i][0])<500):
                acc2 = acc2+int(num_list2[i][0])
                print(num_list2[i][0])
                bag_acc2+=1
        print("总计卡包数："+str(bag_acc+bag_acc2))
        print("总计卡牌数："+str(acc+acc2))
        print("OCG卡包数："+str(bag_acc))
        print("OCG卡牌数："+str(acc))
        print("TCG卡包数："+str(bag_acc2))
        print("TCG卡牌数："+str(acc2))