

def check_recovered_values(int_list_old, int_list_new):
    assert len(int_list_old) == len(int_list_new), "recovered integers are different lengths than original, Abort!"

    for i in range(0, len(int_list_old)):
        assert int_list_old[i] == int_list_new[i], "recovered integers don't match at "+str(i)


def create_image_from_int_list(int_list, _BYTES):
    length = len(int_list)
    image_bytes = bytearray()

    for i in range(0, length):
        _bytes_array = bytearray(int(int_list[i]).to_bytes(_BYTES, byteorder='little'))
        if i == length - 1:
            image_bytes.extend(_bytes_array)
            f2 = open("data/flower2.jpg", "wb")
            f2.write(image_bytes)
            f2.close()
            break

        else:
            image_bytes.extend(_bytes_array)

