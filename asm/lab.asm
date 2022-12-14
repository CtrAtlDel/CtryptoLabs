ORG 8000H
MOV SP, #60H
IEN0 EQU 0A8H

LJMP START

ORG 8003H ;обработчик прерывания INT0
    LCALL TIMER_REDIRECT
    RETI
ORG 800BH    ;обработчик прерывания при переполнении таймера Т0
    CLR TF0  ;сброс флага переполнения таймера Т0
    INC DPTR ;увеличение программного счетчика
    MOV A,DPH
    SWAP A ;для корректного отображения на индикаторе
    MOV 0C0h,A  ;вывод старшего байта программного счетчика на индикацию
    RETI ;возвращается на адрес, сохраненный в RETI
START:
    MOV IE,#83h ;разрешение прерывания при переполнении таймера Т0 и INT0
    MOV DPTR,#0000h ;сброс программного счетчика
    LJMP $     ;безусловный переход, предварительно сохранив значение адреса команды в стек вызовов
    CLR TR0 ;сброс бита разрешения таймера Т0
    CLR TF0 ;сброс флага переполнения таймера Т0
    MOV TL0, #00h
    MOV TH0, #00h
    MOV TMOD, #09h ;Т0 таймер в режиме 1 с запуском по единичному значению на входе INT0
    MOV TCON, #00h ; INT0 по низкому уровню
    MOV R0, #00h
    SETB TR0   ;разрешение работы таймера Т0
TIMER_REDIRECT:

    RET
END