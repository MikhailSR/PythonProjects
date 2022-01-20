import PyPDF2


object = open("test.pdf", "rb")
reader = PyPDF2.PdfFileReader(object)
page1 = reader.getPage(0)
text = page1.extractText()
print(text)

# String = "заключении несколько слов о генераторе случайных чисел в Python. Доступ к генераторуслучайных чисел осуществляется путем импорта"

# for i in range(0, NumPages):
#     PageObj = object.getPage(i)
#     print("this is page " + str(i))
#     Text = PageObj.extractText()
#     # print(Text)
#     ResSearch = re.search(String, Text)
#     print(ResSearch)
