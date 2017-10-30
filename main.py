import CSVWorker
import thread
import WordsCounter

LINE_TO_READ = 3


def callback_function(first_counter, second_counter):
    # type: (WordsCounter,  WordsCounter) -> WordsCounter
    print "start callback"
    first_counter + second_counter
    print "end callback"




file_to_read = 'input2.txt'
input_file = open(file_to_read, 'r')
first = WordsCounter.WordsCounter()
i = 0
for line in input_file:
    print ("send " + str(i) + " buffer: |" +line + "|\n")
    i += 1
    second = WordsCounter.WordsCounter(line)
    thread.start_new_thread(second.calculate, (callback_function, [first, second]))

print "after sending loop"
print first.get_result()
CSVWorker.dict_to_csv(first.get_result())
input_file.close()
print 'Done!'
