from datetime import datetime, date


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

