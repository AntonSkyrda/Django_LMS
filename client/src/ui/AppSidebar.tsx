import { Home, Folders, Users, ClipboardList, Sheet } from "lucide-react";

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
} from "../ui/Sidebar";

const items = [
  {
    title: "Головна",
    url: "home",
    icon: Home,
  },
  {
    title: "Курси",
    url: "courses",
    icon: Folders,
  },
  {
    title: "Групи",
    url: "groups",
    icon: Users,
  },
  {
    title: "Заняття",
    url: "lessons",
    icon: Sheet,
  },
  {
    title: "Завдання",
    url: "tasks",
    icon: ClipboardList,
  },
];

export default function AppSidebar() {
  return (
    <Sidebar collapsible="icon">
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Навігація</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton tooltip={item.title} asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarRail />
    </Sidebar>
  );
}
