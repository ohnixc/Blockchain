from pprint import pprint

"""
data: {
    'pair_1': {...},
    'pair_2': {...},
    . . . . .
}


data[pair] = {
    'exch_name_1': {...},
    'exch_name_2': {...},
    . . . . .
}


data[pair][exch] = {
    'asks': [
        [price_with_fee, volume, original_price],
        ...
    ],
    'bids': [
        [price_with_fee, volume, original_price],
        ...
    ]
}
"""


def _join_and_sort(data_pair, order_type):
    """
    :param data_pair: dictionary, data[pair] -- see example at the beginning of this file
    :return: array
    """
    ans = []
    for exch in data_pair.keys():
        for order in data_pair[exch][order_type]:
            order.append(exch)
            ans.append(order)
    if order_type == 'bids':
        ans.sort(key=lambda quad: quad[0], reverse=True)   # bids sorted in descending order by price
    else:
        ans.sort(key=lambda quad: quad[0])                 # asks sorted in ascending order by price
    return ans


def join_and_sort(data):
    ans = dict()
    for pair in data.keys():
        ans[pair] = dict()
        ans[pair]['asks'] = _join_and_sort(data[pair], 'asks')
        ans[pair]['bids'] = _join_and_sort(data[pair], 'bids')
    return ans


# data = {
#     'bch_btc': {
#         'cex': {
#             'asks': [
#                          [0.11493361749999999, 0.12743832, 0.114647],
#                          [0.11493461999999999, 0.1, 0.114648],
#                          [0.1149356225, 4.0, 0.114649]
#                     ],
#             'bids': [
#                          [0.11376786750000001, 0.01, 0.114053],
#                          [0.11376687, 4.0, 0.114052],
#                          [0.1137658725, 0.4, 0.114051]
#                     ]
#             },
#         'exmo': {
#             'asks': [
#                         [0.11540177286, 0.14055705, 0.11517143],
#                         [0.11544253422, 0.00300111, 0.11521211],
#                         [0.11544255426, 0.05773397, 0.11521213]
#                     ],
#             'bids': [
#                         [0.11395380566, 0.00185455, 0.11418217],
#                         [0.11389567216, 0.2693056, 0.11412392],
#                         [0.11359313843999999, 0.19522126, 0.11382078]
#                     ]
#         }
#     },
#     'bch_usd': {
#         'cex': {
#             'asks': [
#                         [706.50185, 4.0, 704.74],
#                         [706.5118749999999, 0.30848692, 704.75],
#                         [706.8126249999999, 1.7032, 705.05]
#                     ],
#             'bids': [
#                         [698.9682, 4.0, 700.72],
#                         [698.9582250000001, 1.42481089, 700.71],
#                         [698.94825, 2.283186, 700.7]
#                     ]
#         },
#         'exmo': {
#             'asks': [
#                         [703.99842229164, 0.03648861, 702.59323582],
#                         [705.8728571986801, 2.91, 704.46392934],
#                         [705.8728572087, 1.069, 704.46392935]
#                     ],
#             'bids': [
#                         [694.9607747865, 0.8348454, 696.35348175],
#                         [694.9573, 19.0, 696.35],
#                         [694.92317454768, 0.33, 696.31580616]
#             ]
#         },
#         'kraken': {
#             'asks': [
#                         [700.71714, 0.375, 698.9],
#                         [701.41896, 0.08, 699.6],
#                         [701.51922, 0.565, 699.7]
#                     ],
#             'bids': [
#                         [695.4870199999999, 1.99, 697.3],
#                         [695.1877999999999, 0.139, 697.0],
#                         [695.0880599999999, 2.39, 696.9]
#                     ]
#         }
#     }
# }
#
#
# pprint(join_and_sort(data))