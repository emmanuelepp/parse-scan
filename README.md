# parse-scan

Extract open ports from nmap, masscan, and rustscan output files.

## Usage

```bash
python3 parse_scan.py <scan_file>
```

## Example

```bash
$ python3 parse_scan.py scan.nmap
22,80,443,3306,8080
```

Pipe directly into another nmap scan:

```bash
nmap -sV -sC -p $(python3 parse_scan.py scan.nmap) 10.10.10.10
```

## Supported formats

- nmap normal output (`-oN`)
- nmap greppable output (`-oG`)
- masscan greppable output (`-oG`)
- rustscan output

## Requirements

Python 3.6+