def can_place_video_ads(feed_items, n):
    if n == 0:
        return True

    length = len(feed_items)
    max_ads = 0

    # Проверяем все позиции для вставки (перед, между, после)
    for i in range(length + 1):
        # Проверяем соседей слева и справа
        left_ok = (i == 0) or (feed_items[i - 1] not in (1, 2))
        right_ok = (i == length) or (feed_items[i] not in (1, 2))

        if left_ok and right_ok:
            max_ads += 1

    return max_ads >= n

feed_items_input = input().strip()
n = int(input().strip())

feed_items = list(map(int, feed_items_input.strip('[]').split(',')))

result = can_place_video_ads(feed_items, n)
print(str(result))