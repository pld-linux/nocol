Summary:	Network Operation Center On-Line
Name:		nocol
Version:	4.3.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NOCOL/SNIPS (Network Operation Center On-Line) is a network monitoring
package that runs on Unix platforms and is capable of monitoring network and
system variables such as ICMP or RPC reachability, RMON variables,
nameservers, ethernet load, port reachability, host performance, SNMP traps,
modem line usage, appletalk & novell routes/services, BGP peers, syslog
files, etc. The software is extensible and new monitors can be added easily.

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
$RPM_OPT_FLAGS -I/usr/include/ncurses
yacc
/usr/bin/perl
EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
