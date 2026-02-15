#!/usr/bin/env python3
import argparse
import pandas as pd
import os


def xlsx_to_csv(input_file, output_dir=None):
    xlsx = pd.ExcelFile(input_file)
    
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(input_file))
    
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    for sheet in xlsx.sheet_names:
        df = pd.read_excel(xlsx, sheet_name=sheet)
        output_file = os.path.join(output_dir, f"{base_name}_{sheet}.csv")
        df.to_csv(output_file, index=False)
        print(f"Created {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert XLSX to CSV")
    parser.add_argument("input", help="Input XLSX file")
    parser.add_argument("-o", "--output-dir", help="Output directory (default: same as input)")
    args = parser.parse_args()
    
    xlsx_to_csv(args.input, args.output_dir)
