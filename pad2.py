import cv2


def pad(src, patch, left_top, right_bot):
    h1, w1 = src.shape[0], src.shape[1]

    h = right_bot[0] - left_top[0]
    w = right_bot[1] - left_top[1]

    if h > h1 or w > w1:
        print("错误:检查填充大小!")
        return src
    else:
        patch = cv2.resize(patch, (w, h))
        src[left_top[0]:right_bot[0], left_top[1]:right_bot[1], :] = patch
        return src


if __name__ == "__main__":
    src = cv2.imread('1.png')
    patch = cv2.imread('2.png')
    save_path = 'save.png'
    dst = pad(src, patch, [100, 500], [1111, 1555])
    cv2.imwrite(save_path, dst)
    print('Done')

