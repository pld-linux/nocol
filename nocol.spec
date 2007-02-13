Summary:	Network Operation Center On-Line
Summary(pl.UTF-8):	Centrum Operacji Sieciowych
Name:		nocol
Version:	4.3.1
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.netplex-tech.com/software/nocol/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	e054261e64f7683b5661f42ad37db15e
URL:		http://www.netplex-tech.com/software/nocol/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NOCOL/SNIPS (Network Operation Center On-Line) is a network monitoring
package that runs on Unix platforms and is capable of monitoring
network and system variables such as ICMP or RPC reachability, RMON
variables, nameservers, ethernet load, port reachability, host
performance, SNMP traps, modem line usage, appletalk & novell
routes/services, BGP peers, syslog files, etc. The software is
extensible and new monitors can be added easily.

%description -l pl.UTF-8
NOCOL/SNIPS (Network Operation Center On-Line) jest pakietem
monitorującym sieć działającym na uniksach, który może monitorować
sieć i takie cechy systemu jak osiągalność ICMP czy RPC, zmienne RMON,
serwery DNS, obciążenie sieci, osiągalność portów, wydajność
komputera, pułapki SNMP, obciążenie linii modemowej, serwisy AppleTalk
i Novell, połączenia BGP, pliki logów itp. To oprogramowanie jest
rozszerzalne i nowe monitory mogą być dodawane w prosty sposób.

%prep
%setup -q

%build
cat | ./Configure <<EOF
%{_prefix}
%{_mandir}

localhost
/bin/mail
root@localhost
root@localhost
gcc
%{rpmcflags} -I/usr/include/ncurses
yacc
%{_bindir}/perl
EOF

%{__make} << EOF
%{__make}
EOF

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
