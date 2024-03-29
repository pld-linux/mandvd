Summary:	ManDVD - DVD video creator
Summary(de.UTF-8):	ManDVD - DVD Video Kreator
Summary(pl.UTF-8):	ManDVD - kreator DVD video
Name:		mandvd
Version:	2.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://csgib36.ifrance.com/FTP/%{name}-%{version}src.tar.gz
# Source0-md5:	64b958fd703fd1cfbce70f03b5d8ae12
Source1:	%{name}.desktop
URL:		http://www.kde-apps.org/content/show.php?content=38347
BuildRequires:	qmake >= 6:3.3
BuildRequires:	qt-devel >= 6:3.3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	ImageMagick >= 1:6.2.4
Requires:	cdrtools-mkisofs >= 5:2.01
Requires:	dvd+rw-tools >= 5.21.4
Requires:	dvd-slideshow
Requires:	dvdauthor >= 0.6.11
Requires:	lame >= 3.97
Requires:	mencoder >= 3:1.0
Requires:	mjpegtools >= 1.8.0
Requires:	mplayer >= 3:1.0
Requires:	netpbm >= 10.29
Requires:	transcode >= 1.0.2
Requires:	xine-lib > 2:0.99.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program to simply create DVD Video.

%description -l de.UTF-8
Dies ist ein Programm zum einfachen erstellen von DVD Videos.

%description -l pl.UTF-8
To program do łatwego tworzenia DVD video.

%prep
%setup -q -n ManDVD-%{version}src

%build
export QTDIR=%{_prefix}
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}
install mandvd $RPM_BUILD_ROOT%{_bindir}/mandvd
install mandvdico.png $RPM_BUILD_ROOT%{_pixmapsdir}/mandvdico.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mandvd
%{_pixmapsdir}/mandvdico.png
%{_desktopdir}/%{name}.desktop
