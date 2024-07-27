//
// Created by ASUS on 24-7-26.
//
#include <stm32f10x.h>
#include "car.h"

void stop(void)
{
    GPIO_WriteBit(GPIOD,GPIO_Pin_4,0);
    GPIO_WriteBit(GPIOD,GPIO_Pin_2,0);
}

void go(void)
{
    GPIO_WriteBit(GPIOD,GPIO_Pin_4,1);
    GPIO_WriteBit(GPIOD,GPIO_Pin_2,1);
}

void run(void)
{
    GPIO_WriteBit(GPIOC,GPIO_Pin_11,1);
    GPIO_WriteBit(GPIOD,GPIO_Pin_0,0);
    GPIO_WriteBit(GPIOD,GPIO_Pin_6,1);
    GPIO_WriteBit(GPIOG,GPIO_Pin_9,0);

}
void back(void)
{
    GPIO_WriteBit(GPIOC,GPIO_Pin_11,0);
    GPIO_WriteBit(GPIOD,GPIO_Pin_0,1);
    GPIO_WriteBit(GPIOD,GPIO_Pin_6,0);
    GPIO_WriteBit(GPIOG,GPIO_Pin_9,1);
}

void left(void)
{
    GPIO_WriteBit(GPIOC,GPIO_Pin_11,0);
    GPIO_WriteBit(GPIOD,GPIO_Pin_0,1);
    GPIO_WriteBit(GPIOD,GPIO_Pin_6,1);
    GPIO_WriteBit(GPIOG,GPIO_Pin_9,0);
}

void right(void)
{
    GPIO_WriteBit(GPIOC,GPIO_Pin_11,1);
    GPIO_WriteBit(GPIOD,GPIO_Pin_0,0);
    GPIO_WriteBit(GPIOD,GPIO_Pin_6,0);
    GPIO_WriteBit(GPIOG,GPIO_Pin_9,1);
}

