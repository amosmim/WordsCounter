import CSVWorker

import WordsCounter

LINE_TO_READ = 5


def callback_function(first_counter, second_counter):
    # type: (WordsCounter,  WordsCounter) -> WordsCounter
    first_counter + second_counter


file_to_read = 'input2.txt'
input_file = open(file_to_read, 'r')
buffer_list = input_file.readlines(LINE_TO_READ)
buffer_tmp = ''
for string in buffer_list:
    buffer_tmp += string + '\n'

first = WordsCounter.WordsCounter(buffer_tmp)
first.calculate()

buffer_list = input_file.readlines(LINE_TO_READ)
while buffer_list:
    buffer_tmp = ''
    for string in buffer_list:
        buffer_tmp += string + '\n'
    second = WordsCounter.WordsCounter(buffer_tmp)
    second.calculate(callback_function, [first, second])
    buffer_list = input_file.readlines(LINE_TO_READ)

CSVWorker.dict_to_csv(first.get_result())
input_file.close()
print 'Done!'
