import os
import subprocess
import threading
import queue

def main():
    # funcion Cambio de directorio
    os.chdir("C:\\Club Car Programming\\firmware\\adb\\1.8.2")
    # funcion revisar dispositivos conectados
    try:
        output = subprocess.check_output("uuu -lsusb", shell=True, text=True)
        print("Salida de uuu -lsusb:\n")
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar 'uuu -lsusb': {e}")
    # funcion subir android a dispositivos
    print("Ejecutando uuu_imx_android_flash.bat -f imx8mm -a -e -u ddr4 -d ddr4...")

    def enqueue_output(src, out, queue):
        for line in iter(out.readline, ''):
            queue.put(line)
        out.close()

    process = subprocess.Popen("uuu_imx_android_flash.bat -f imx8mm -a -e -u ddr4 -d ddr4",
                               shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    q_stdout = queue.Queue()
    q_stderr = queue.Queue()

    stdout_thread = threading.Thread(target=enqueue_output, args=('stdout', process.stdout, q_stdout))
    stderr_thread = threading.Thread(target=enqueue_output, args=('stderr', process.stderr, q_stderr))

    stdout_thread.daemon = True
    stderr_thread.daemon = True

    stdout_thread.start()
    stderr_thread.start()

    output = ""
    
    while process.poll() is None:
        while not q_stdout.empty():
            line = q_stdout.get_nowait()
            print(line, end='')
            output += line  # agregar la línea a la variable de salida

        while not q_stderr.empty():
            line = q_stderr.get_nowait()
            print(line, end='')
            output += line  # agregar la línea a la variable de salida

    # Imprimir cualquier salida restante después de que el proceso haya finalizado
    while not q_stdout.empty():
        line = q_stdout.get_nowait()
        print("1" + q_stdout.get_nowait(), end='')
        line = q_stdout.get_nowait()

    while not q_stderr.empty():
        line = q_stderr.get_nowait()
        print(line, end='')
        output += line  # agregar la línea a la variable de salida
    
    # buscar "Start Cmd:FB: done" en la variable de salida
    if "Start Cmd:FB: done" in output:
        print("programación exitosa")
    else:
        print("programación fallida")

    # funcion aplicaciones

if __name__ == "__main__":
    main()