import optparse
import nmap

def nmapScan(tgtHost, tgtPort):
        nScan = nmap.PortScanner()
        nScan.scan(tgtHost, tgtPort)
        state = nscan[tgtHost]['tcp'][int(tgtPort)]['state']
        print "[+]" +tgtHost+ "tcp/" + tgtPort + " " + state


def Main():
        praser = optparse.OptionParser('usage %prog -H <target host>' +\
                                       '-P <target port>')
        praser.add_option('-H', dest='tgtHost', type = 'string', \
                          help = 'specify target host')
        praser.add_option('-P', dest='tgtPort', type = 'string', \
                          help = 'specify target port[s] seperated by a comma, seperate range with a dash')\
        (options, args) = parser.parser_args()

        if (option.tgtHost == None) | (option,tgtPort == None):
                print praser.usage
                exit(0)
        else:
                tgtHost = option.tgtHost
                if '-' in str(option.tgtPort):
                        tgtPort = option.tgtPort.split('-')
                        tgtPort = range(int(tgtPort[0]), int(tgtPort[1]))
                else:
                        tgtPort = str(option.tgtPort).split('-')

        for tgtPort in tgtPorts:
                nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
        Main()

