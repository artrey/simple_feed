from django import template

register = template.Library()


@register.filter
def minus(value: float, subtrahend: float) -> float:
    return value - subtrahend


@register.filter
def mult(value: float, factor: float) -> float:
    return value * factor
