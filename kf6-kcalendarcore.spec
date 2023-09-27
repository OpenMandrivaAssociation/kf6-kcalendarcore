%define libname %mklibname KF6CalendarCore
%define devname %mklibname KF6CalendarCore -d
%define git 20230927

Name: kf6-kcalendarcore
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kcalendarcore/-/archive/master/kcalendarcore-master.tar.bz2#/kcalendarcore-%{git}.tar.bz2
Summary: Library for Interfacing with Calendars
URL: https://invent.kde.org/frameworks/kcalendarcore
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: pkgconfig(libical)
Requires: %{libname} = %{EVRD}

%description
Library for Interfacing with Calendars

%package -n %{libname}
Summary: Library for Interfacing with Calendars
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library for Interfacing with Calendars

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for Interfacing with Calendars

%prep
%autosetup -p1 -n kcalendarcore-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kcalendarcore.*

%files -n %{devname}
%{_includedir}/KF6/KCalendarCore
%{_libdir}/cmake/KF6CalendarCore
%{_qtdir}/mkspecs/modules/qt_KCalendarCore.pri
%{_qtdir}/doc/KF6CalendarCore.*
%{_libdir}/pkgconfig/KF6CalendarCore.pc

%files -n %{libname}
%{_libdir}/libKF6CalendarCore.so*
