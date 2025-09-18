using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace hello_world
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n, contapar, contaimpar, num; // variables de tipo entero
            contapar = 0;
            contaimpar = 0;
            Console.WriteLine("Digite cantidad de numeros");
            n = int.Parse(Console.ReadLine());
            Console.WriteLine(); //linea en blanco

            for (int i = 0; i < n; i++) 
            {
               Console.WriteLine("Digite un numero");
                num = int.Parse(Console.ReadLine());

                if (num % 2 == 0)
                {
                   contapar++; 
                }
                else
                {
                    contaimpar++;
                }
                Console.WriteLine(); //linea en blanco
                Console.WriteLine("la cantidad de numeros pares es {0} y la cantidad de impares es {1}", contapar,contaimpar);
                Console.ReadKey(true);
            }
        }
    }
}
