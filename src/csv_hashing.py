"""CSVファイルを単純にハッシュ化する

特定の値に対して、必ず１つの値が確定する。
そのため、例えば「1234」という値が複数回登場するとしたら、
そのハッシュ値は必ず同じ値になる。
"""

import csv
import hashlib
from operator import mod

def csv_hashing(in_file_name:str, column_index:list[int], out_file_name:str, header_row:int=1) -> None:
    """CSVファイルの特定の列をハッシュ化する

    Args:
        in_file_name (str): 入力CSVファイル. utf-8である前提.
        column_index (list[int]): ハッシュ化する列のindex. 0ベース.
        out_file_name (str): 出力CSVファイル. utf-8.
        header_row (int): ヘッダ行数.
    """
    if False:   # for debug
        print('in: {in_file_name}\ncolumn: [{columns}]\nout: {out_file_name}'
            .format(
                in_file_name = in_file_name,
                columns = ', '.join([str(i) for i in column_index]),
                out_file_name = out_file_name
            ))
    
    with open(in_file_name, mode='r', encoding='utf-8') as f_in:
        with open(out_file_name, mode='w', encoding='utf-8') as f_out:
            reader = csv.reader(f_in)
            for i, row in enumerate(reader):
                if i>=header_row:
                    # 指定した列のみハッシュ化
                    for col in column_index:
                        row[col] = val_hashing(row[col])
                f_out.write(','.join(row)+'\n')
    
    return None


def val_hashing(base_str: str) -> str:
    """文字列をハッシュ化する

    Args:
        base_str (str): ハッシュ化前の文字列

    Returns:
        str: ハッシュ化後の文字列
    """
    return hashlib.sha3_256(base_str.encode()).hexdigest()


if __name__=='__main__':
    in_file_name = './input/test1.csv'
    out_file_name = './output/test1_out.csv'
    column_index = [0,1]
    csv_hashing(in_file_name, column_index, out_file_name)

