def main():
    text= input("prompt")
    
    print('{}=funktion.funktion("Add", "MathNode", self)'.format(text))
    print('        {}p1=parameter.parameter("Value1", "Number")'.format(text))
    print('        {}p2=parameter.parameter("Value2", "Number")'.format(text))
    print('        {}Out=parameter.parameter("Result", "Number")'.format(text))
    print('        {}.parameterList.append({}p1)'.format(text,text))
    print('        {}.parameterList.append({}p2)'.format(text,text))
    print('        {}.setOutput({}Out)'.format(text,text))
    print('        self.funktionsList[{}.getName()] = {}'.format(text,text))


if __name__ == '__main__':
    main()