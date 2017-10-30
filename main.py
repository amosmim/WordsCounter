import CSVWorker
import thread
import WordsCounter

LINE_TO_READ = 3


def callback_function(first_counter, second_counter):
    # type: (WordsCounter,  WordsCounter) -> WordsCounter
    first_counter + second_counter





file_to_read = 'input2.txt'
input_file = open(file_to_read, 'r')
first = WordsCounter.WordsCounter()

for line in input_file:
    second = WordsCounter.WordsCounter(line)
    thread.start_new_thread(second.calculate, (callback_function, [first, second]))


CSVWorker.dict_to_csv(first.get_result())
input_file.close()
print 'Done!'
