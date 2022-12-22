ORG 8000H ;change < 8000H for debug

IEN0 EQU 0A8H

LJMP START
ORG 8003H           ;обработчик прерывания INT0
    LCALL TIMER_REDIRECT
    RETI
ORG 800BH           ;обработчик прерывания при переполнении таймера Т0
    CLR TF0         ;сброс флага переполнения таймера Т0
    INC R2          ;увеличение программного счетчика
    MOV A, DPH 
    SWAP A          ;для корректного отображения на индикаторе
    MOV 0C0h,A      ;вывод старшего байта программного счетчика на индикацию
    RETI            ;возвращается на адрес, сохраненный в RETI
TIMER_REDIRECT:
    MOV R0,#00h
    MOV R2,#000h    ;сброс программного счетчика
    CLR TR0         ;сброс бита разрешения таймера Т0
    CLR TF0         ;сброс флага переполнения таймера Т0
    SETB TR0        ;разрешение работы таймера Т0
    MOV A, DPH 
    SWAP A 
    RET
START:
    MOV SP, #60H
    MOV R0,#00h      ;сброс программмного счетчика
    MOV IE,#83h      ;разрешение прерывания при переполнении таймера Т0
    MOV R2,#000h     ;сброс программного счетчика R2 R3 - разрядный
    CLR TR0          ;сброс бита разрешения таймера Т0
    CLR TF0          ;сброс флага переполнения таймера Т0
    MOV TL0, #00h
    MOV TH0, #00h
    MOV TMOD,#09h    ;Т0 таймер в режиме 1 с запуском по единичному значению на входе INT0
    SETB TR0         ;разрешение работы таймера Т0
    SETB IT0
    LJMP $           ;безусловный переход, предварительно сохранив значение адреса команды в 