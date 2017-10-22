
def dict_to_csv(dict_obj, first_line=None, output_file_name='output.csv'):
    cvs_file = open(output_file_name, 'w')
    cvs_format = '{},{}\n'
    if first_line:
        cvs_file.write(cvs_format.format(first_line[0].capitalize(), first_line[1].capitalize()))
    for pair in dict_obj.items():
        cvs_file.write(cvs_format.format(pair[0], pair[1]))
    cvs_file.close()


def csv_to_dict(file_name, delete_first_coulm_flag = False):
    # type: (str) -> dict

    cvs_file = open(file_name, 'r')
    tmp_dict = {}
    line = cvs_file.readline()
    while line:
        pair = line.split(',')
        tmp_b = pair[1].strip('\n\r ')
        try:
            tmp_dict[pair[0]] = int(tmp_b)
        except:
            try:
                tmp_dict[pair[0]] = float(tmp_b)
            except:
                tmp_dict[pair[0]] = tmp_b
        line = cvs_file.readline()
    cvs_file.close()
    if delete_first_coulm_flag:
        del tmp_dict[tmp_dict.keys()[0]]
    return tmp_dict


def lib_test():
    test_file_name = 'output2.csv'
    tmp_dict = {'Amos': 99, 'Chen': 70, 'Koko': 50, 'Maayan': 100, 'Adi': 88}
    dict_to_csv(tmp_dict, ['name', 'Grade'], test_file_name)
    result = csv_to_dict(test_file_name, True)
    print "Length : %d" % len(tmp_dict)
    if len(result) != len(tmp_dict):
        print 'ERROR in lib_test : different length! %d , %d' % len(result) , len(tmp_dict)
        return
    for key in result.keys():
        if key not in tmp_dict or tmp_dict[key] != result[key]:
            print 'ERROR in lib_test : in key %s!' % key
            return
    print 'lib_test Succeeded!'

