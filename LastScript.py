import pandas as pd
import re

df = pd.read_csv('Plugin_Details_6 copy.csv')
version_pattern = re.compile("\d+(?:[\.,](\d+|\*|))*.*")

lst_new_col = []
lst_solution = df['Solution'].to_list()

for item in lst_solution:

        Product1 = re.search('Upgrade to (.+?) version (.+?) or later', str(item))
        if Product1:
            item = "Upgrade "+Product1.group(1)+" to the latest version"
            lst_new_col.append(item)
            continue

        Product2 = re.search('Upgrade to (.+?) or later', str(item))
        if Product2:
            group = Product2.group(1)
            group_element = group.split(" ")
            output = []
            for element in group_element:
                if version_pattern.search(element):
                    break
                output.append(element)

            final_element = " ".join(output)
            item = "Upgrade " + final_element + " to the latest version"
            lst_new_col.append(item)
            continue

        Product3 = re.search('Update to (.+?) version (.+?) or later', str(item))
        if Product3:
            item = "Update " + Product3.group(1) + " to the latest version"
            lst_new_col.append(item)
            continue

        Product4 = re.search('Update to (.+?) or later', str(item))
        if Product4:
            group = Product4.group(1)
            group_element = group.split(" ")
            output = []
            for element in group_element:
                if version_pattern.search(element):
                    break
                output.append(element)

            final_element = " ".join(output)
            item = "Update " + final_element + " to the latest version"
            lst_new_col.append(item)
            continue
        else:
            lst_new_col.append('')

print(lst_new_col)
df['NewCol'] = lst_new_col


df.to_csv('Plugin_Details_6 copy22.csv', index=False)

newdf = pd.read_csv('Plugin_Details_6 copy22.csv')
newdf.head(5)




