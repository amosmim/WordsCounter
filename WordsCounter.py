import thread


class WordsCounter:
    """
    This Class counts repetition of words in given text buffer.
    not reusable.
    """
    def __init__(self, buffer_to_count='', dict_to_start_with=None):
        """
        constructor
        :param buffer_to_count: text to count words from (Optional)
        :param dict_to_start_with: dict object to merge results with (Optional)
        """
        self._words_dict = dict_to_start_with
        self._buffer = buffer_to_count
        self._started = False
        self._done = False
        self._callback = None
        self._callback_args = []
        self._lock = thread.allocate_lock()

    def calculate(self, callback=None, callback_args=[]):
        """
        count function.
        :param callback: callable to call when done. (Optional)
        :param callback_args: args to input to callable. (Optional)
        :return: None
        """
        # type: (callable(list), list) -> None

        self._lock.acquire()
        if not self._callback:
            self._callback = callback
            self._callback_args = callback_args
        if not self._words_dict:
            self._words_dict = {}
        self._started = True
        if not self._done:
            if self._buffer == '':
                self._done = True
                self._lock.release()
                return
            word_list_in_buffer = self._buffer.split()
            for word in word_list_in_buffer:
                fix_word = word.strip(',.-*+/-~`()=$#^%&:;><?\'\"').lower()

                if fix_word == '':
                    continue
                if fix_word not in self._words_dict:
                    self._words_dict[fix_word] = 1
                else:
                    self._words_dict[fix_word] += 1
            self._done = True

            self._lock.release()
            if self._callback:
                if self._callback_args:
                    self._callback(self._callback_args[0], self._callback_args[1])
                else:
                    self._callback()

        else:
            self._lock.release()


    def __add__(self, other):
        """
        Merge 2 WordsCounter's dictionaries
        :type other: WordsCounter
        """
        # type: WordsCounter -> WordsCounter

        while not self._done or not other._done:
            if not self._started:
                self.calculate()
            if not other._started:
                other.calculate()

        self._lock.acquire()
        other._lock.acquire()
        for key in other._words_dict.keys():

            if key in self._words_dict:
                self._words_dict[key] = self._words_dict[key] + other._words_dict[key]
            else:
                self._words_dict[key] = other._words_dict[key]

        other._lock.release()
        self._lock.release()
        return self

    def get_result(self):
        """
        getter for dict with the words count.
        :return: dict
        """
        # type: () -> dict

        while not self._done:
            pass

        self._lock.acquire()
        copy = self._words_dict
        self._lock.release()
        return copy