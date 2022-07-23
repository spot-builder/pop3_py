import poplib
import sys
from cmd import Cmd

if len(sys.argv) == 5:
    try:
        pop = poplib.POP3(host=sys.argv[1], port=int(sys.argv[2]))
        pop.user(sys.argv[3])
        pop.pass_(sys.argv[4])
        stat = pop.stat()
        print(f"Total: {stat[0]} messages\nSize: {stat[1]}")


        class Pop3(Cmd):
            """Pop3 message extractor"""
            prompt = "pop3> "
            print("Type message number")

            def default(self, args):
                cmd = args.replace('"', '\\"')
                retrieved_message = pop.retr(cmd)
                print(f"{retrieved_message[0].decode()}\n")
                retrieved_str = ''
                for i in retrieved_message[1]:
                    retrieved_str += f"{i.decode()}\n"
                print(retrieved_str)

            def do_exit(self, args):
                """Exit"""
                return True


        term = Pop3()
        term.cmdloop()
    except poplib.error_proto as ex:
        print(ex)
else:
    print("Usage:\npython main.py host port user pass")
